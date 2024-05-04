package Simulation;

public class Place {
    //Each coordinate on the plane
    int position[] = new int[2];
    int food;
    boolean isOccupied = false;
    Place(int food, int position[]){
        this.food = food;
        this.position = position;
    }
    

}

