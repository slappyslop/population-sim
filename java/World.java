package Simulation;
import java.util.ArrayList;
import java.util.Random;

    


public class World {

    public static Place[][] places;
    public static ArrayList<Blob> blobs = new ArrayList<Blob>();
    public static Random rand = new Random();

    static void initialize(int dim, int initial_pop) {  //Takes in initial population and dimension of plane, spits out a list of blob objects and place objects


        places = new Place[dim][dim];
        int i, j;

        for (i = 0; i < dim; i++) {    // Initalizes a list of place objects whose index corresponds to its position
            for (j = 0; j < dim; j++) {
                int[] position = {i, j};
                places[i][j] = new Place(rand.nextInt(5), position);
            }
        }
        for (i = 0; i < initial_pop; ) { // initalizes a list of blobs
            blobs.ensureCapacity(initial_pop);
            int[] possible_location = {rand.nextInt(dim), rand.nextInt(dim)};
            if (!places[possible_location[0]][possible_location[1]].isOccupied) { // checks if possible locations are occupied, if not, then tries again
                blobs.add(new Blob(0, possible_location));
                places[possible_location[0]][possible_location[1]].isOccupied = true;
                i++;
            }


        }

    }

    public static void mainly(String[] args) {
        World.initialize(4, 1);
        blobs.get(0).build_posArr();
        System.out.println(blobs.get(0).location[0] + " " + blobs.get(0).location[1]);



    }


    public static void main(String args[]) {
        World.initialize(3, 2);
        int i = 0;
        for (;i<800;) {
            if (i ==  6) {
                System.out.println("here");
            }
            i++;
            System.out.println("\n\nIteration: " + i+ "Population" + blobs.size());
            int l = blobs.size();
            for (int j=0; j<l;) {
                Blob b = blobs.get(j);
                b.nourishment -=1;
                if (b.willDie()) { // kill blobs marked for death
                    blobs.remove(b);
                    l = l-1;
                    continue;

                }

                b.feed();
                b.build_posArr();
                b.reproduce();
                b.movable.clear();


                j++;
                System.out.println(b.location[0]+ " "+ b.location[1] + "    " + b.nourishment);

            }

        }
    }
}

