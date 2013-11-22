def testUKSchedule():
    click("1385148178359.png")
    wait(1)
    type("chrome")
    type(Key.ENTER)
    wait(3)
    click("1385149223037.png")
    
    type("www.ukathletics.com")
    type(Key.ENTER)
    wait(2)
    hover("1385148252568.png")
    click(Pattern("mensmenu.png").targetOffset(0,19))
    row = find("1385148577223.png")
    assert row.exists("1385149293255.png")

testUKSchedule()