package Simulation;

public class Main {
    public static void main(String args[]) {
        World world = new World(3, 2);

        int i = 0;
        while (!world.blobs.isEmpty()) {
            i++;
            System.out.println("\n\nIteration: " + i+ "Population" + world.blobs.size());
            int l = world.blobs.size();
            for (int j=0; j<l;) {
                Blob b = world.blobs.get(j);
                b.nourishment -=1;
                if (b.willDie()) { // kill blobs marked for death
                    world.blobs.remove(b);
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
