package ir.skings.simplehttp;

import android.os.AsyncTask;
import android.support.annotation.BoolRes;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity {

    private TextView amount;
    private ImageView led;
    private ModuleAsyncTask mat;
    private LedAsyncTask lat;
    private int ledStat;
    private Timer t ;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initiate();

    }

    public void initiate(){
        // find views
        amount = (TextView) findViewById(R.id.amount_tv);
        led = (ImageView) findViewById(R.id.led_iv);

        // run for first time
        mat = new ModuleAsyncTask();
        mat.execute();
        lat = new LedAsyncTask();
        lat.execute("read");

        // set onclick for led image
        led.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Trigger ledstat between 0 and 1 for write mode
                ledStat = (ledStat+1)%2;
                lat = new LedAsyncTask();
                lat.execute("write",ledStat+"");
            }
        });

        //Check for new amount of module
        //Declare the timer
        t = new Timer();
        //Set the schedule function and rate
        t.scheduleAtFixedRate(new TimerTask() {
                                  @Override
                                  public void run() {
                                      mat = new ModuleAsyncTask();
                                      mat.execute();
                                  }

                              },
                //Set how long before to start calling the TimerTask (in milliseconds)
                0,
                //Set the amount of time between each execution (in milliseconds)
                1000);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        t.cancel();
    }

    private class ModuleAsyncTask extends AsyncTask<String,Integer,Double>{
        String st;
        @Override
        protected Double doInBackground(String... params) {
            URL url;
            HttpURLConnection urlConnection = null;
            try {
                url = new URL("http://thingtalk.ir/channels/99/feed.json?key=FSM9WRHECVOVXZ5D");

                urlConnection = (HttpURLConnection) url
                        .openConnection();

                InputStream in = urlConnection.getInputStream();
                InputStreamReader isr = new InputStreamReader(in);
                BufferedReader br = new BufferedReader(isr);

                String input = br.readLine();
                // thing talk json maker
                ThingTalkJSON ttj = new ThingTalkJSON(input);
                if(ttj.getFeeds().size() > 0) {
                    st = (String) ttj.getFeeds().get(ttj.getFeeds().size() - 1).get("field1");
                }else {
                    Log.d("SKings", "channel is empty");
                    st = "";
                }
                Log.d("SKings",st);


                br.close();
                isr.close();
                in.close();

            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (urlConnection != null) {
                    urlConnection.disconnect();
                }
            }
            return null;
        }

        @Override
        protected void onPostExecute(Double aDouble) {
            super.onPostExecute(aDouble);
            amount.setText(st);
        }

    }

    private class LedAsyncTask extends AsyncTask<String,Integer,Double>{

        @Override
        protected Double doInBackground(String... params) {
            URL url;
            HttpURLConnection urlConnection = null;
            try {
                if(params[0].equals("write")){
                    String writeUrl = "http://thingtalk.ir/update?key=22MD2PEIDDSAJQN7&field1=";
                    writeUrl += ledStat;
                    url = new URL(writeUrl);

                    urlConnection = (HttpURLConnection) url
                            .openConnection();

                    InputStream in = urlConnection.getInputStream();
                    InputStreamReader isr = new InputStreamReader(in);
                    BufferedReader br = new BufferedReader(isr);

                    br.readLine();

                    br.close();
                    isr.close();
                    in.close();
                }else{
                    url = new URL("http://thingtalk.ir/channels/100/feed.json?key=22MD2PEIDDSAJQN7");

                    urlConnection = (HttpURLConnection) url
                            .openConnection();

                    InputStream in = urlConnection.getInputStream();
                    InputStreamReader isr = new InputStreamReader(in);
                    BufferedReader br = new BufferedReader(isr);

                    String input = br.readLine();
                    // thing talk json maker
                    ThingTalkJSON ttj = new ThingTalkJSON(input);
                    // set ledstat in read mode
                    if(ttj.getFeeds().size() > 0) {
                        ledStat = Integer.parseInt((String) ttj.getFeeds().get(ttj.getFeeds().size() - 1).get("field1"));
                    }else {
                        Log.d("SKings","channel is empty");
                        ledStat = 0;
                    }
                    Log.d("SKings",ledStat + "");

                    br.close();
                    isr.close();
                    in.close();
                }


            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (urlConnection != null) {
                    urlConnection.disconnect();
                }
            }
            return null;
        }

        @Override
        protected void onPostExecute(Double aDouble) {
            super.onPostExecute(aDouble);
            if(ledStat == 1){
                led.setImageResource(R.drawable.led_on);
            }else{
                led.setImageResource(R.drawable.led_off);
            }
        }

    }
}
