# COMPUTADORES = {
#         "COMP0": "NOTEBOOK",
#         "COMP1": "DELL-ED",
#         "COMP2": "UNI-CAROL",
#         "COMP3": "DELL-EL",
#         "COMP4": "EASYPC-ED",
#         "COMP5": "SERV01",
#         "COMP6": "SERV02",
#         "COMP7": "SERV03"
# }

# COMP_PARAM = [
#         {"nome": "COMP0", "bases": ["A", "B"], "blocos": 128, "modos":["ECB"]},
#         {"nome": "COMP3", "bases": ["C", "D"], "blocos": 128, "modos":["ECB"]},

#         {"nome": "COMP4", "bases": ["A", "B"], "blocos": 256, "modos":["ECB", "CBC", "CFB", "OFB", "CTR"]},
#         {"nome": "COMP1", "bases": ["C", "D"], "blocos": 256, "modos":["ECB", "CBC", "CFB", "OFB", "CTR"]},

#         {"nome": "COMP2", "bases": ["A", "B"], "blocos": 384, "modos":["ECB", "CBC", "CFB", "OFB", "CTR"]},
#         {"nome": "COMP5", "bases": ["C", "D"], "blocos": 384, "modos":["ECB", "CBC", "CFB", "OFB", "CTR"]},

#         {"nome": "COMP6", "bases": ["A", "B"], "blocos": 512, "modos":["ECB", "CBC", "CFB", "OFB", "CTR"]},
#         {"nome": "COMP7", "bases": ["C", "D"], "blocos": 512, "modos":["ECB", "CBC", "CFB", "OFB", "CTR"]}
#     ]

COMP_PARAM = [
        {"nome": "COMP0", "bases": ["A", "B"], "blocos": 64, "modos":{"AES":[], "DES":["ECB"]}},
        {"nome": "COMP1", "bases": ["C", "D"], "blocos": 64, "modos":{"AES":[], "DES":["ECB"]}},

        {"nome": "COMP2", "bases": ["A", "B"], "blocos": 128, "modos":{"AES":["ECB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}},
        {"nome": "COMP3", "bases": ["C", "D"], "blocos": 128, "modos":{"AES":["ECB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}},

        {"nome": "COMP4", "bases": ["A", "B"], "blocos": 256, "modos":{"AES":["ECB", "CBC", "OFB", "CTR", "CFB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}},
        {"nome": "COMP5", "bases": ["C", "D"], "blocos": 256, "modos":{"AES":["ECB", "CBC", "OFB", "CTR", "CFB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}},

        {"nome": "COMP6", "bases": ["A", "B"], "blocos": 384, "modos":{"AES":["ECB", "CBC", "OFB", "CTR", "CFB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}},
        {"nome": "COMP7", "bases": ["C", "D"], "blocos": 384, "modos":{"AES":["ECB", "CBC", "OFB", "CTR", "CFB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}},

        {"nome": "COMP8", "bases": ["A", "B"], "blocos": 512, "modos":{"AES":["ECB", "CBC", "OFB", "CTR", "CFB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}},
        {"nome": "COMP9", "bases": ["C", "D"], "blocos": 512, "modos":{"AES":["ECB", "CBC", "OFB", "CTR", "CFB"], "DES":["ECB", "CBC", "OFB", "CTR", "CFB"]}}
]