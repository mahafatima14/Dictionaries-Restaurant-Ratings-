scores_dict = {}

def output_restaurant_ratings_az():
    """Restaurant rating lister."""
        
    scores = open('scores.txt')
   

    for line in scores:
        line = line.rstrip() 
        restaurant, score = line.split(":")
        #print(restaurant, score)

        scores_dict[restaurant] = int(score)
    
    for resturant, rating in sorted(scores_dict.items()):
        print(f"{resturant} is rated at {rating}")
        
    print()
    print()

def user_input(dictionary):
    """Prompt the user for a new restaurant and rating"""

    user_choice_restaurant = input("Please enter the restaurant of your choice: ")
    user_ratings = int(input("Please enter the ratings: "))

    scores_dict[user_choice_restaurant] = user_ratings
    print()
    output_restaurant_ratings_az()  

output_restaurant_ratings_az()  
user_input(scores_dict)



    
    # print(sorted(scores_dict.items()))
    # sorted_scores = sorted(scores_dict.items())

        

    


    

    #     poem = open(poem_file)

    #     poem_dict = {}

    #     for line in poem:                                   #iterate over each line in the filecd
    #         line = line.rstrip()                            #remove right white space
    #         word_list = line.split(" ")                     #split each line by |
        

    #         for word in word_list:
    #             poem_dict[word] = poem_dict.get(word, 0) + 1
        
    #     for word, count in poem_dict.items():
    #         print(f'{word}: {count}')
                
    #     return poem_dict


    # get_word_count_from_poem("twain.txt")




