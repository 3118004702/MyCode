package com.example.myapplication;

import com.google.gson.JsonIOException;

import org.json.JSONException;
import org.json.JSONObject;

public class Weather {
    private String city;
    private String cityid;
    private String temp;
    private String WD;
    private String WS;
    private String SD;
    private String AP;
    private String time;

    public String getCity() {
        return city;
    }

    public String getCityid() {
        return cityid;
    }

    public String getAP() {
        return AP;
    }

    public String getSD() {
        return SD;
    }

    public String getTemp() {
        return temp;
    }

    public String getTime() {
        return time;
    }

    public String getWD() {
        return WD;
    }

    public String getWS() {
        return WS;
    }

    public void setCityid(String cityid) {
        this.cityid = cityid;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setAP(String AP) {
        this.AP = AP;
    }

    public void setSD(String SD) {
        this.SD = SD;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public void setWD(String WD) {
        this.WD = WD;
    }

    public void setWS(String WS) {
        this.WS = WS;
    }
}
