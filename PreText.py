# Python Dictionary 

statements = {'1': """
Hello,

I have picked up your ticket. I would like to set up a Teams call, and a TeamViewer session to solve your ticket issue. Are you available?""", 
# 1 is the Ticket Starter.
    
    '2':"""
I am escalating your ticket to Application Support. They are the primary group in charge of handling this platform, and can answer any questions in further detail.""",  
# 2 is the send to App Support.

    '3':"""
Hello again, 

Are you still needing help on the issue of this ticket? All tickets close after no response for 3 days. Let me know how we can best get a hold of you. Thanks.""", 
# 3 is the 3rd day reminder.

    '4':"""
Hello,

There seems to be a wider spread problem with this issue. Your ticket will now be linked to the reported problem for a faster recovery. We have our top experts on working on the solution, and we hope to have this platform up shortly.""", 
# 4 is the outage statement.

    '5':"""
Hello,

I will be excalating your ticket to your local I.T. district office, because this issue may need inperson, and a hands on hardware solution. They should be getting a hold of you shortly.""", 
# 5 is the send to local I.T.



# Porgrams from HotKeys:

    '1p':"""
runas /user:matta cleanmgr.exe""", # Admin DiskClean.

    '2p':"""
runas /user:matta powershell.exe""", # Admin PowerShell.

}
