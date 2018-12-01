public class Main {

    public static void main(String[] args) throws Exception {
        HttpURLConnectionClass http = new HttpURLConnectionClass();
        int fuelLevel = http.getFuel();
        double[] location = http.getLocation();
        int[] tirePressure = http.getTirePressure();
        System.out.println(fuelLevel);
        System.out.println(location[0]);
        System.out.println(tirePressure[0]);
    }
}
