import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpURLConnectionClass {
    public JSONObject GET(String parameter) {
        try {
            String url = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles/AF795E35CFFCE82E48/" + parameter;
            String token = "39b9c134-4313-47f5-a6d3-edda592c6b18";
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();

            con.setRequestMethod("GET");
            con.setRequestProperty("accept", "application/json");
            con.setRequestProperty("authorization", "Bearer " + token);

            int responseCode = con.getResponseCode();

            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            //System.out.println(response);
            JSONObject res = new JSONObject(response.toString());
            return res;
        }
        catch(Exception exception) {
            System.out.println("An error has been occured.");
            return null;
        }
    }
    
    public int getFuel() {
         JSONObject fuelLevelPercent = GET("fuel");
         int fuelLevel = fuelLevelPercent.getJSONObject("fuellevelpercent").getInt("value");
         return fuelLevel;
    }
    
    public double[] getLocation() {
         JSONObject location = GET("location");
         double longitude = location.getJSONObject("longitude").getDouble("value");
         double latitude = location.getJSONObject("latitude").getDouble("value");
         double heading = location.getJSONObject("heading").getDouble("value");
         double coordinates[] = {longitude, latitude, heading};
        return coordinates;
    }
    
    public int[] getTirePressure() {
         JSONObject tirePressure = GET("tires");
         int rearleft = tirePressure.getJSONObject("tirepressurerearleft").getInt("value");
         int rearright = tirePressure.getJSONObject("tirepressurerearright").getInt("value");
         int frontright = tirePressure.getJSONObject("tirepressurefrontright").getInt("value");
         int frontleft = tirePressure.getJSONObject("tirepressurefrontleft").getInt("value");
         int tirespressure[] = {rearleft, rearright, frontright, frontleft};
         return tirespressure;
    }

}