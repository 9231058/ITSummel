package ir.skings.simplehttp;

import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

/**
 * Created by SKings on 8/20/2016.
 */
public class ThingTalkJSON {
    private ArrayList<HashMap> feeds;

    public ThingTalkJSON(String JSON) throws JSONException {
        // initiate feeds
        feeds = new ArrayList<>();
        // parse json
        JSONObject root = new JSONObject(JSON);
        Log.d("SKings-root",root.toString());

        JSONArray feedsArray = root.getJSONArray("feeds");
        Log.d("SKings-feeds",feedsArray.toString());

        // make fields and add it in array
        for (int i = 0; i < feedsArray.length(); i++){
            JSONObject item = new JSONObject(feedsArray.getString(i));
            Log.d("SKings-item",item.toString());
            HashMap fields = new HashMap();
            Iterator<String> keys = item.keys();
            // iterate over keys
            while (keys.hasNext()){
                String key = keys.next();
                Log.d("SKings-key",key+">"+item.get(key));
                fields.put(key,item.get(key));
            }

            // add Hashmap to feeds
            feeds.add(fields);
        }
    }

    public ArrayList<HashMap> getFeeds() {
        return feeds;
    }

    public void setFeeds(ArrayList<HashMap> feeds) {
        this.feeds = feeds;
    }
}
