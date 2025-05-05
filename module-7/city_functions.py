#Juedeja Richard - Module7.2 -4/27/25
#This program will return a single string in the form of City,Country at least 3 times

def format_city_country(city_name, country_name, language_type="unknown", population_num="population"):
    set1 = city_name
    set2 = country_name
    set3 = language_type
    set4 = population_num

    location = set1 + ',' + set2 + ',' + 'population'+ '-'+ set4 + ',' + set3

    return location
#created function to make format country,city,language and population

#make a main function
def main():
#get input for variables from the user
    city_name = input("What is the city?")
    country_name = input("What is the Country?")
    language_type = input("What language do they speak?")
    population_num = int(input("How big is the population?"))
    print("This is the Location 3 times:")

#will print output up to 3 times

    for i in range(1):
        print(f"{city_name.title()},{country_name.title()}")
        print(f"{city_name.title()},{country_name.title()}, population - {population_num}")
        print(f"{city_name.title()},{country_name.title()},{language_type.title()}, population - {population_num}")
#use f string to concatenate int and strings together

if __name__== '__main__':
    main()
#call the main function