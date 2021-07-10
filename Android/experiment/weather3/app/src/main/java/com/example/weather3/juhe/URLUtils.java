package com.example.weather3.juhe;

public class URLUtils {

    public static String url = "http://wthrcdn.etouch.cn/weather_mini?city=";

    public static String getTemp_url(String city){
        String url1 = url + city;
        return url1;
    }
}
