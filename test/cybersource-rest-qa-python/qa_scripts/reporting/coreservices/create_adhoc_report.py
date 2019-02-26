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


def create_adhoc_report():
    with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "reporting", "coreservices",
                           "create_adhoc_report.csv"), newline='') as csvfile:  # current folder is MainTestPackage
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(reader)
        for row in reader:

            with open(os.path.join(os.getcwd(), "qa_scripts", "csv_files", "test_report", "testresults.csv"), 'a',
                      newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                config_obj = configuration.InputConfiguration()
                details_dict1 = config_obj.get_configuration()
                api_instance = ReportsApi(details_dict1)
                tcid = row[0]
                definition_name = row[1]
                reportname = row[2]
                starttime = row[3]
                endtime = row[4]
                message = row[5]

                # Setting the json message body
                request = RequestBody1()
                request.report_definition_name = definition_name
                request.timezone = "GMT"
                request.report_mime_type = "application/xml"
                request.report_name = reportname
                request.report_start_time = starttime
                request.report_end_time = endtime
                request.report_filters = {
                    "Application.Name": []
                }
                request.report_preferences = {"signedAmounts": "true", "fieldNameConvention": "SOAPI"}
                request.report_fields = ["Request.RequestID", "Request.TransactionDate", "Request.MerchantID"]
                message_body = json.dumps(request.__dict__)

                # payment_request = AuthorizeNetRest.PaymentRequest("true", amount_detail, "", payment_instrument, baseaddress_bill_to, baseaddress_ship_to, ip, order, "", "", "", lineitem)
                try:
                    api_response = api_instance.create_report(message_body)

                    if (api_response):
                        writer.writerow([tcid, "CreateAdhocReport", "Passed:" + str(api_response.status), message

                                            , datetime.datetime.now()])

                except ApiException as e:
                    size = len(row)
                    if (row[size - 1] == "Negative" and str(e.status) == '400'):

                        writer.writerow(
                            [tcid, "CreateAdhocReport", "Failed:" + str(e.status),
                             json.loads(e.body)['message'] + ":" + message, datetime.datetime.now()])
                    else:
                        writer.writerow(
                            [tcid, "CreateAdhocReport", "Failed:" + str(e.status),
                             json.loads(e.body)['message'] + ":" + message, datetime.datetime.now()])
                except Exception as ex:

                    writer.writerow([tcid, "CreateAdhocReport", ex, datetime.datetime.now()])


if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_adhoc_report()
