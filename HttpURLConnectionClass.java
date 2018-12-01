import java.io.*;
import java.net.*;
import java.util.*;

public class HttpURLConnectionClass {
     public void sendGet() throws Exception {
          try {
               String url = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles/AF795E35CFFCE82E48/fuel";
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
               System.out.println(response.toString());
          }
          catch(Exception exception) {
               System.out.println("An error has been occured.");
          }
     }
     public static void main(String[] args) throws Exception {
          HttpURLConnectionClass http = new HttpURLConnectionClass();
		http.sendGet();
     }
}