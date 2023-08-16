package Simulation;
import java.util.Random;
class Blob {
    // beings in the program
    int age, nourishment;
    boolean canReproduce;
    int location[] = new int[2];

    Blob(int age, int [] locations){
        this.age = age;
        nourishment = 8; 
        this.location = locations;
                
    }

    boolean checkReproducing(){
        if (nourishment>7){
            nourishment -= 5;
            return true;
        }
        else return false;
    }


    
}

 class blobex{

    static void initialize(int dim, int initial_pop){  //Takes in initial population and dimension of plane, spits out a list of blob objects and place objects 

        Random rand = new Random();
        Place places[][] = new Place[dim][dim];
        Blob blobs[] = new Blob[initial_pop]; 
        int i, j = 0;

        for (i=0;i<dim;i++){    // Initalizes a list of place objects who's index corresponds to its position
            for (j=0;j<dim; j++){
                int[] position = {i, j};
                places[i][j] = new Place(rand.nextInt(6), position);
            }
        }
        for (i=0;i<initial_pop;){ // initalizes a list of blobs
            int possible_location[] = {rand.nextInt(dim), rand.nextInt(dim)};
            if (!places[possible_location[0]][possible_location[1]].isOccupied){ // checks if possible locations are occupied, if not, then tries again
                blobs[i] = new Blob(0, possible_location);
                places[possible_location[0]][possible_location[1]].isOccupied = true;
                i++;
            }
            else continue;                

        } 

    } 

    public static void main(String args[]){
        initialize(10, 10);
       
        
    
    }
}