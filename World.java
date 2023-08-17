package Simulation;
import java.util.ArrayList;
import java.util.Random;

    


public class World{
        
    public static Place places[][];
    public static ArrayList<Blob> blobs = new ArrayList<Blob>(); 

    static void initialize(int dim, int initial_pop){  //Takes in initial population and dimension of plane, spits out a list of blob objects and place objects 

        Random rand = new Random();
        places = new Place[dim][dim];
        int i, j = 0;

        for (i=0;i<dim;i++){    // Initalizes a list of place objects who's index corresponds to its position
            for (j=0;j<dim; j++){
                int[] position = {i, j};
                places[i][j] = new Place(rand.nextInt(6), position);
            }
        }
        for (i=0;i<initial_pop;){ // initalizes a list of blobs
            blobs.ensureCapacity(initial_pop);
            int possible_location[] = {rand.nextInt(dim), rand.nextInt(dim)};
            if (!places[possible_location[0]][possible_location[1]].isOccupied){ // checks if possible locations are occupied, if not, then tries again
                blobs.add(new Blob(0, possible_location));
                places[possible_location[0]][possible_location[1]].isOccupied = true;
                i++;
            }
            else continue;                  

        } 

    } 

    public static void main(String args[]){
        World.initialize(3, 1);
        blobs.get(0).build_posArr();
        System.out.println(blobs.get(0).location[0] + " " + blobs.get(0).location[1]);
        for (int x=0; x<3; x++){
            for(int y=0; y<3; y++){
                System.out.print(blobs.get(0).posArr[x][y]+ " ");
                
            }
            System.out.print("\n");
        }
    }
    
    
    
    
    
    public static void mainacc(String args[]){
        World.initialize(1, 1);
        int i = 0;
        while (blobs.size()!= 0){
            i++;                   
            for (Blob b : blobs){
                b.updateFlags();
                if (b.willDie){ // kill blobs marked for death
                    blobs.remove(b);
                    continue;
                }
                b.feed();
            }

        }
    }
          
}

