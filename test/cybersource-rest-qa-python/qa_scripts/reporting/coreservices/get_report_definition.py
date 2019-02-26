from __future__ import print_function
import os
import sys
import csv
from CyberSource import *
from CyberSource.rest import ApiException
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()
util_file = os.path.join(os.getcwd(), "qa_scripts", "utility", "constant_utility.py")
utility = SourceFileLoader("module.name", util_file).load_module()
import datetime


def get_report_definitions():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "reporting", "coreservices",
                           "get_report_definition.csv"), newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = ReportDefinitionsApi(details_dict1)
                tcid = row[0]
                report_definition_name = row[1]
                message = row[2]
                try:
                    api_response = api_instance.get_resource_info_by_report_definition(report_definition_name)

                    if (api_response):
                        api_response_data = json.loads(api_response.data)
                        # QA modification
                        if api_response_data["reportDefintionName"] == report_definition_name:
                            # QA modification
                            writer.writerow([tcid, "GetReportDefinition", "Passed:" + str(api_response.status), message

                                                , datetime.datetime.now()])
                        # print(amount)
                        else:
                            writer.writerow(
                                [tcid, "GetReportDefinition", "Assertion Failed: " + str(api_response.status),
                                 datetime.datetime.now()])

                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "GetReportDefinition", "Failed:" + str(e.status), message, datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "GetReportDefinition", "Failed:" + str(e.status)
                                , message, datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "GetReportDefinition", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_report_definitions()
