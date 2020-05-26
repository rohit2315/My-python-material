game_on=True

while game_on==True:
    
    new_round=True
    
    player={'Name':'Hulk','Attack':10,'Heal':16,'Health':100}
    monster={'Name':'Thanos','Attack':12,'Health':100}

    
    print('Enter name')
    player['Name'] = input()
    monster['Name']
    
    while new_round==True:

        player_won=False
        monster_won=False


        print('Select Action:')
        print('1)Attack')
        print('2)Heal')
        print('3)Exit')


       
        player_choice=input()


        if player_choice=='1':
            monster['Health']=monster['Health']-player['Attack']
            
            if monster['Health']<=0:
                player_won=True
           
            else:
                player['Health']=player['Health']-monster['Attack'] 
                
                if player['Health']<=0:
                    monster_won=True
        
        elif player_choice=='2':
            print('Heal player') 


        elif player_choice=='3':
            new_round=False
            game_on=False

        
        else:
            print('Invalid Input') 

        if player_won==True or monster_won==True:
             new_round=False    



