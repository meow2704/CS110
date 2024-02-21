#Omyaasree Balaji
#Lab-4 Files And Functions
#CS110  


def steps_analyzer(file):
    steps_total = 0
    steps_max = 0

    for steps_function in range(7): #need the loop to iterate 7 times only
        steps = int(file.readline())
        steps_total = steps_total+steps

        if steps_max < steps: #max() function cannot be used here as it works only for lists or assigned set of variables
            steps_max = steps

    return steps_total, steps_max



def heart_rate_analyzer(file):
    heart_rate_total = 0

    for heart_function in range(7): #need the loop to iterate 7 times only
        heart_rate = int(file.readline())
        heart_rate_total = heart_rate_total + heart_rate

    average_heart_rate = heart_rate_total / 7
    return average_heart_rate



def sleep_analyzer(file):
    sleep_total = 0
    sleep_min = 25  #setting it to 25 as the number of hours cannot exceed 24

    for sleep_function in range(7):
        sleep_hours = float(file.readline())
        sleep_total = sleep_total + sleep_hours

        if sleep_hours < sleep_min:  #min() function cannot be used here as it works only for lists or assigned set of variables
            sleep_min = sleep_hours

    return sleep_total, sleep_min



def write_results_file(steps_total, steps_max, average_heart_rate, sleep_total, sleep_min): #parameters can have any names

    fitness_handler = open("results.txt", "a") #using append because we are creating as well as writing into that file
    fitness_handler.write(f"The total number of steps taken this week were: {steps_total}.\n")
    fitness_handler.write(f"The maximum number of steps taken this week were: {steps_max}.\n")
    fitness_handler.write(f"The average heart rate for the week was: {average_heart_rate:.2f}.\n") 
    fitness_handler.write(f"The total number of hours slept this week was: {sleep_total:.2f}.\n")
    fitness_handler.write(f"The least amount of hours slept this week was: {sleep_min:.2f}.\n")
    #returns a decimal value which may not terminate(hence :.2f)



def main():

    infile = open("fitness_data.txt", "r")   #infule = input file = fitness_data file

    steps_total, steps_max = steps_analyzer(infile)

    average_heart_rate = heart_rate_analyzer(infile)

    sleep_total, sleep_min = sleep_analyzer(infile)

    write_results_file(steps_total, steps_max, average_heart_rate, sleep_total, sleep_min)

main()