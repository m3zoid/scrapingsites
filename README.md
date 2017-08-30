Task is to write a BOT, which can extract odds/probability for all the teams in World Cup 2018 Win Outright market from links give below and generate a real-time matrix from it. Code should either print matrix to screen or save it in file, which should update at given interval (by default every 5 minutes). Preferably use text processing/analysis to navigate to correct match link from home URL instead of hardcoding the start URL. Team names can also be used as parameter (expected given) to locate correct odds elements on page.

For example the matrix should have following format:

            Site1   Site2   Site3
    Team1   odds    odds    odds
    Team2   odds    odds    odds
    Team3   odds    odds    odds


Points will be given based on:
1. Code correctness 
2. Code design and architecture
3. Speed of execution


List of web pages to extract odds from are as follows:

1. http://sports.williamhill.com/bet/en-gb/betting/e/1644903/World+Cup+2018+-+Outright.html
2. https://www.skybet.com/football/world-cup-2018/event/16742642
3. http://www.paddypower.com/football/international-football/world-cup-2018?ev_oc_grp_ids=1828129
4. https://mobile.bet365.com/#type=Coupon;key=1-172-1-26326924-2-0-0-0-2-0-0-0-0-0-1-0-0-0-0-0-0;ip=0;lng=1;anim=1
