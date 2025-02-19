package Simulation;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

    


public class World {

    public  Place[][] places;
    public  List<Blob> blobs = new ArrayList<Blob>();
    public  Random rand = new Random();

    public World(int dim, int initial_pop) {  //Takes in initial population and dimension of plane, spits out a list of blob objects and place objects


        places = new Place[dim][dim];
        int i, j;

        for (i = 0; i < dim; i++) {    // Initalizes a list of place objects whose index corresponds to its position
            for (j = 0; j < dim; j++) {
                int[] position = {i, j};
                places[i][j] = new Place(rand.nextInt(5), position);
            }
        }
        for (i = 0; i < initial_pop; ) { // initalizes a list of blobs
            int[] possible_location = {rand.nextInt(dim), rand.nextInt(dim)};
            if (!places[possible_location[0]][possible_location[1]].isOccupied) { // checks if possible locations are occupied, if not, then tries again
                blobs.add(new Blob(0, possible_location, this));
                places[possible_location[0]][possible_location[1]].isOccupied = true;
                i++;
            }


        }

    }



}

