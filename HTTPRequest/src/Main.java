import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;




public class Main {

    public static void main(String[] args) throws Exception {
        HttpURLConnectionClass http = new HttpURLConnectionClass();
        JSONObject response = http.sendGet();
        System.out.println(fuelLevel);
    }
}
