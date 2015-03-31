__author__ = 'Beni'

test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71, "APPL"],
]

appl = []

msft = []

for i in test_data:
    ticker_symbol = i[1]
    if "APPL" == ticker_symbol:
        appl.append(i)
    else:
        msft.append(i)

print(appl)
print(msft)

# test_data = [
#     ["2014-06-01", "APPL", 100.11],
#     ["2014-06-01", "APPL", 110.61],
#     ["2014-06-01", "APPL", 120.22],
#     ["2014-06-01", "APPL", 100.54],
#     ["2014-06-01", "MSFT", 20.46],
#     ["2014-06-01", "MSFT", 21.25],
#     ["2014-06-01", "MSFT", 32.53],
#     ["2014-06-01", "MSFT", 40.71],
#     ["2014-04-01", "BLAH", 19.99],
#     ["2014-09-01", "BLAH", 29.99],
# ]
#
# appl = []
#
# msft = []
#
# for data in test_data:
#
#     temp = []
#
#     if data[1] == "APPL":
#         temp.append(data[0])
#         temp.append(data[2])
#         appl.append(temp)
#     elif data[1] == "MSFT":
#         temp.append(data[0])
#         temp.append(data[2])
#         msft.append(temp)
#
# print(appl)
# print(msft)

