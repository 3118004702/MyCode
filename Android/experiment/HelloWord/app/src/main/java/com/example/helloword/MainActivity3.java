package com.example.helloword;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.Toolbar;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MainActivity3 extends AppCompatActivity {

//    private ListView news_category;
    private  ListView news_list;
    @Override

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
//        news_category = (ListView) findViewById(R.id.news_category);
//        news_category.setAdapter(new ArrayAdapter<String>(this,
//                R.layout.support_simple_spinner_dropdown_item,getResources().getStringArray(R.array.news_category)));
    news_list = (ListView) findViewById(R.id.news_list);
    SimpleAdapter adapter = new SimpleAdapter(this,getData(),R.layout.list_item,
            new String[]{"news_title","news_info","news_thumb"},
            new int[]{R.id.news_title,R.id.news_info,R.id.news_thumb});
    news_list.setAdapter(adapter);
    }
    private List<Map<String, Object>> getData(){             //将四个输入内容转换成list显示
        List<Map<String, Object>> list = new ArrayList<Map<String, Object>>();
        Map<String,Object> map = new HashMap<String, Object>();
        map.put("news_title","广东工业大学");
        map.put("news_info","大学城中间");
        map.put("news_thumb",R.drawable.gd);
        list.add(map);

        map = new HashMap<String, Object>();
        map.put("news_title","广州美术学院");
        map.put("news_info","广工旁边");
        map.put("news_thumb",R.drawable.guangmei);
        list.add(map);

        map = new HashMap<String, Object>();
        map.put("news_title","广州大学");
        map.put("news_info","大学城西");
        map.put("news_thumb",R.drawable.guangda);
        list.add(map);

        map = new HashMap<String, Object>();
        map.put("news_title","华南理工大学");
        map.put("news_info","大学城南");
        map.put("news_thumb",R.drawable.huanna);
        list.add(map);
        return list;
    }
}