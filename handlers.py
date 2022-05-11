

errors = [

    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div/span/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div/span/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div/span/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div/span/div",
    "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div"

]

error_fixes = {
    "SPELLING" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div"
    ],

    "VOCABULARY" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div"
    ],

    "PUNCTUATION" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div"
    ],

    "CONCISENESS" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/span/div"
    ],

    "CLARITY" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div[2]/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/nav/div[4]",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div[2]/div"
    ],

    "VARIETY" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div"
    ],

    "GRAMMAR" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/span/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div"
    ],

    "READABILITY" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div"
    ],

    "CONVENTIONS" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div[2]/div",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/span/div"
    ],

    "CONSISTENCY" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div[2]"
    ],

    "ACCEPT" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[3]/div[2]"
    ],

    "DELETE" : [
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/nav/div[4]",
        "//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/div/nav/div[5]"
    ]    
}