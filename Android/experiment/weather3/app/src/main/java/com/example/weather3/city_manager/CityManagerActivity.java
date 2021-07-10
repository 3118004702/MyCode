package com.example.weather3.city_manager;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Toast;

import com.example.weather3.R;
import com.example.weather3.bean.WeatherBean;
import com.example.weather3.db.DBManager;
import com.example.weather3.db.DatabaseBean;

import java.util.ArrayList;
import java.util.List;

public class CityManagerActivity extends AppCompatActivity implements View.OnClickListener{
    ImageView addIv,backIv,deleIv;
    ListView cityLv;
    List<DatabaseBean> mDatas;
    private CityManagerAdapter adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {  //大窗口的初始化框框
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_city_manager);
        addIv = findViewById(R.id.city_iv_add);
        backIv = findViewById(R.id.city_iv_back);
        deleIv = findViewById(R.id.city_iv_delete);
        cityLv = findViewById(R.id.city_lv);
        mDatas = DBManager.queryAllInfo();

        addIv.setOnClickListener(this);
        backIv.setOnClickListener(this);
        deleIv.setOnClickListener(this);
//      设置适配器
        adapter = new CityManagerAdapter(this,mDatas);
        cityLv.setAdapter(adapter);
    }
    //获取数据库数据，添加到原有数据中
    @Override
    protected void onResume() {
        super.onResume();
        List<DatabaseBean> list = DBManager.queryAllInfo();
        mDatas.clear();
        mDatas.addAll(list);
        adapter.notifyDataSetChanged();
    }
    @Override
    public void onClick(View v) {         //添加，返回，删除
        switch (v.getId()){
            case R.id.city_iv_add:
                int cityCount = DBManager.getCityCount();
                if(cityCount < 5) {
                    Intent intent = new Intent(this,SearchCityActivity.class);
                    startActivity(intent);
                }else {
                    Toast.makeText(this,"城市数量已达上限",Toast.LENGTH_SHORT).show();
                }
                break;
            case R.id.city_iv_back:
                finish();
                break;
            case  R.id.city_iv_delete:
                Intent intent1 = new Intent(this, DeleteCityActivity.class);
                startActivity(intent1);
                break;
        }
    }

}