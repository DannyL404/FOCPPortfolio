import sys
import cat_shelter

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print('There is no file selected!')
else:
    cat_shelter.shelter_analysis(sys.argv[1])


