package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.android.volley.NetworkResponse;
import com.android.volley.ParseError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.HttpHeaderParser;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.JsonRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;
import com.google.gson.JsonIOException;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.UnsupportedEncodingException;

public class MainActivity extends AppCompatActivity {

    private TextView tvWeatherCity,tvWeather,tvWeatherTemp,tvImg1,tvImg2;
    private RequestQueue requestQueue;
//    private String weatherinfo="{\"city\":\"北京\",\"cityid\":\"101010100\",\"temp1\":\"-2℃\",\"temp2\":\"16℃\",\"weather\":\"晴\",\"img1\":\"n0.gif\",\"img2\":\"d0.gif\",\"ptime\":\"18:00\"}";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        requestQueue = Volley.newRequestQueue(this);
        init();
        getJSONByVolley();
    }
    public void init() {                     //初始化页面里的几个框
        tvWeatherCity = (TextView)findViewById(R.id.weatherCity);    //地点
        tvWeather = (TextView)findViewById(R.id.weather);            //风向
        tvWeatherTemp = (TextView)findViewById(R.id.weatherTemp);    //气温
        tvImg1 = (TextView)findViewById(R.id.img1);                  //温度
        tvImg2 = (TextView)findViewById(R.id.img2);                  //大气压强


    }

    private void getJSONByVolley() {
        String JSONDataUrl = "http://www.weather.com.cn/data/sk/101280101.html";      //从该网址获取天气数据
        LXJsonObjectRequest jsonObjectRequest = new LXJsonObjectRequest(Request.Method.GET,JSONDataUrl, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
//                            tvWeather.setText(response.toString());
                            JSONObject weatherinfo = response.getJSONObject("weatherinfo");     //数据存储于该主键，读取数据

//                            Weather weather = convertToBean(weatherinfo);
                            Gson gson = new Gson();    //乱码，将json文件转换成字符串，用于提取
                            Weather weather = gson.fromJson(weatherinfo.toString(),Weather.class);  //读取转换后的文件
//                            tvWeatherCity.setText(weather.toString());
                            setWeatherData(weather);   //将转换后的文件进行展示
                        } catch (JsonIOException | JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError volleyError) {

                        volleyError.printStackTrace();
                    }
                }

        );
        requestQueue.add(jsonObjectRequest);
    }
    public  Weather convertToBean(JSONObject json) {
        Weather w = new Weather();
        try {
            w.setCity(json.getString("city"));
            w.setCityid(json.getString("cityid"));
            w.setAP(json.getString("AP"));
            w.setWD(json.getString("WD"));
            w.setTemp(json.getString("temp"));
            w.setWS(json.getString("WS"));
            w.setSD(json.getString("SD"));
            w.setTime(json.getString("time"));
        }catch (JsonIOException | JSONException e) {
            e.printStackTrace();
        }
        return w;
    }

    public  void setWeatherData(Weather weather) {        //框里显示
        tvWeatherCity.setText(weather.getCity());
        tvWeather.setText("风向："+weather.getWD()+"风力："+weather.getWS());
        tvWeatherTemp.setText("气温："+weather.getTemp()+"℃");
        tvImg1.setText("湿度："+weather.getSD());
        tvImg2.setText("大气压强："+weather.getAP());
    }

}
class LXJsonObjectRequest extends JsonObjectRequest {       //转码用的方法


    public LXJsonObjectRequest(int method, String url, JSONObject jsonRequest, Response.Listener<JSONObject> listener, Response.ErrorListener errorListener) {
        super(method, url, jsonRequest, listener, errorListener);
    }

    public LXJsonObjectRequest(String url, JSONObject jsonRequest, Response.Listener<JSONObject> listener, Response.ErrorListener errorListener) {
        super(url, jsonRequest, listener, errorListener);
    }

    /**
     * <p>Description:｛转码｝</p>
     * @author:yangbiyao@163.com
     * @see com.android.volley.toolbox.JsonObjectRequest#parseNetworkResponse(com.android.volley.NetworkResponse)
     */
    @Override
    protected Response<JSONObject> parseNetworkResponse(NetworkResponse response) {
        try {
            response.headers.put("HTTP.CONTENT_TYPE", "utf-8");
//                String jsonString = new String(response.data, HttpHeaderParser.parseCharset(response.headers));
            String jsonString = new String(response.data,"utf-8");
            return Response.success(new JSONObject(jsonString), HttpHeaderParser.parseCacheHeaders(response));
        }
        catch (UnsupportedEncodingException e) {
            return Response.error(new ParseError(e));
        }
        catch (JSONException je) {
            return Response.error(new ParseError(je));
        }
    }

}
