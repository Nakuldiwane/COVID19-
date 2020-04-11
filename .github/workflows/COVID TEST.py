"""This is to get COVID19 test for 3 Users"""
import time
i=0
Data=[]
while i < 3:
    Name=input('\nPlease provide name:')
    q1=input('What is your age:')
    q2=input('Do you have any breathing problem?(Yes/No):')
    q3=input('Are you in contact with any covid patient:')
    if (q2 =='Yes') and (q3== 'Yes') :
        print('\nWait we are giving you a result...')
        time.sleep(2)
        Data.append(Name)
        print('\nUser {}: {} Have high chance of COronoa'.format(i+1,Data[i]))
    elif(q2 =='No') and (q3=='No'):
        print('\nWait we are giving you a result...')
        time.sleep(2)
        Data.append(Name)
        print('\nUser {}: {} Have low chance of COronoa'.format(i+1,Data[i]))
    elif (q2 =='Yes') and (q3== 'No'):
        print('\nWait we are giving you a result...')
        time.sleep(2)
        Data.append(Name)
        print('\nUser {}: {} Have medium chance of COronoa'.format(i+1,Data[i]))
    elif (q2 =='No') and (q3== 'Yes'):
        print('\nWait we are giving you a result...')
        time.sleep(2)
        Data.append(Name)
        print('\nUser {}: {} Have medium chance of COronoa'.format(i+1,Data[i]))      
    i=i+1


     
