package com.example.weather3.db;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import java.util.ArrayList;
import java.util.List;

public class DBManager {
    public static SQLiteDatabase database;
//    初始化数据库信息
    public static  void initDB(Context context) {
        DBHelper dbHelper = new DBHelper(context);
        database = dbHelper.getWritableDatabase();
    }
//    查找数据库城市列表
    public static List<String> queryAllCityName() {
        Cursor cursor = database.query("info",null,null,null,null,null,null);
        List<String>cityList = new ArrayList<>();
        while(cursor.moveToNext()) {
            String city = cursor.getString(cursor.getColumnIndex("city"));
            cityList.add(city);
        }
        return cityList;
    }
//    根据城市名称替换信息内容
    public static int updateInfoByCityName(String city, String content) {
        ContentValues values = new ContentValues();
        values.put("context",content);
        return database.update("info",values,"city=?",new String[]{city});
    }
//    根据城市名查询内容
    public static String queryInfoByCity(String city) {
        Cursor cursor = database.query("info",null,"city=?",new String[]{city},null,null,null);
        if(cursor.getCount() > 0) {
            cursor.moveToFirst();
            String content = cursor.getString(cursor.getColumnIndex("content"));
            return content;
        }
        return null;
    }
    public static long addCityInfo(String city, String content) {
        ContentValues values = new ContentValues();
        values.put("city",city);
        values.put("context",content);
        long id = database.insert("info",null,values);
        database.close();
        return id;
    }
//    存储城市天气最多存储个数
    public static int getCityCount() {
        Cursor cursor = database.query("info",null,null,null,null,null,null);
        int count = cursor.getCount();
        return count;
    }
//    查询数据库中全部信息
    public static List<DatabaseBean>queryAllInfo() {
        Cursor cursor = database.query("info",null,null,
                null,null,null,null);
        List<DatabaseBean> list = new ArrayList<>();
        while(cursor.moveToNext()) {
            int id = cursor.getInt(cursor.getColumnIndex("_id"));
            String city = cursor.getString(cursor.getColumnIndex("city"));
            String content = cursor.getString(cursor.getColumnIndex("context"));
            DatabaseBean bean = new DatabaseBean(id,city,content);
            list.add(bean);
        }
        return list;
    }
    /* 根据城市名称，删除这个城市在数据库当中的数据*/
    public static int deleteInfoByCity(String city){
        return database.delete("info","city=?",new String[]{city});
    }

    /* 删除表当中所有的数据信息*/
    public static void deleteAllInfo(){
        String sql = "delete from info";
        database.execSQL(sql);
    }
}
