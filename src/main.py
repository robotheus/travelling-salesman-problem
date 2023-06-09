import sys
import functions as f

def main():
    print("\nGenetic algorithm applied to the traveling salesman problem.\n")
    
    try:
        graphCities = f.start(sys.argv[1])
    except:
        print(f'File "{sys.argv[1]}" not found.')
        return
    
    f.geneticAlgorithm(graphCities)

main()