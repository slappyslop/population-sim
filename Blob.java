package Simulation;

class Blob {
    // beings in the program
    int age, nourishment;
    boolean canReproduce, isHungry, willDie, isSuffocated; 
    int location[] = new int[2];
    boolean[][] posArr = new boolean[3][3];
    Blob(int age, int [] locations){
        this.age = age;
        nourishment = 8; 
        this.location = locations;
                
    }
    //updates eating and reproduction thresholds
    void updateFlags(){ 
        canReproduce = nourishment>7?true:false;
        isHungry = nourishment<10?true:false;
        willDie = nourishment==0?true:false;
        
    }

    void build_posArr(){ // Fills a 2 dimensional array where true is a place that the blob can move, and the middle element is the current positon of the blob
        posArr[1][1] = false;
        for (int x = -1; x<2; x++){
            for(int y = -1; y<2; y++){
                try{
                    posArr[1+x][1+y] = !World.places[location[0]+x][location[1]+y].isOccupied;
                }catch(IndexOutOfBoundsException e){
                     posArr[1+x][1+y] = false;
                }

            }
        }  
        
    }
    
    void feed(){
        if (World.places[location[0]][location[1]].food>0 && isHungry){
            World.places[location[0]][location[1]].food -=1;
            nourishment = 10;
        }
    }

    void reproduce(){
        if (canReproduce ){
        nourishment -= 5;
        
        }



    }
}
