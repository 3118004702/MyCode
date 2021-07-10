package com.example.weather3;

import android.os.Bundle;

import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.example.weather3.base.BaseFragment;
import com.example.weather3.bean.WeatherBean;
import com.example.weather3.db.DBManager;
import com.google.gson.Gson;

import java.util.List;

public class CityWeatherFragment extends BaseFragment {     //获取原始数据
    TextView trmpTv,cityTv,conditionTv,tempRangeTv,dateTv,windTv;
    ImageView dayIv;
    LinearLayout futureLayout;
    String city;
    String url1 = "http://wthrcdn.etouch.cn/weather_mini?city=";
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
     View view = inflater.inflate(R.layout.fragment_city_weather,container,false);
     initView(view);
     Bundle bundle = getArguments();
     city = bundle.getString("city");
     String url = url1+city;
     loadData(url);
     return view;
    }

    @Override
    public void onSuccess(String result) {
//         解析有、并获得数据
        parseShowData(result);
//        更新数据
        int i = DBManager.updateInfoByCityName(city,result);

        if(i <= 0) {
//            没有数据
            DBManager.addCityInfo(city,result);
        }
    }

    @Override
    public void onError(Throwable ex, boolean isOnCallback) { //失败操作
        String s = DBManager.queryInfoByCity(city);
        if(!TextUtils.isEmpty(s)) {
            parseShowData(s);
        }
    }
    private void parseShowData(String result) {      //数据展示
        WeatherBean weatherBean = new Gson().fromJson(result,WeatherBean.class);
        WeatherBean.DataDTO dataDTO = weatherBean.getData();
        WeatherBean.DataDTO.ForecastDTO today = dataDTO.getForecast().get(0);
        dateTv.setText(today.getDate());
        cityTv.setText(dataDTO.getCity());
        windTv.setText(today.getFengxiang());
        tempRangeTv.setText(today.getLow()+'~'+today.getHigh());
        conditionTv.setText(today.getType());
        trmpTv.setText(dataDTO.getWendu()+"℃");
//        获取未来天气加入到layout
        List<WeatherBean.DataDTO.ForecastDTO> futureList = dataDTO.getForecast();
        for (int i = 0; i < futureList.size(); i++) {
            View itemView = LayoutInflater.from(getActivity()).inflate(R.layout.item_main_center, null);
            itemView.setLayoutParams(new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT));
            futureLayout.addView(itemView);
            TextView idateTv = itemView.findViewById(R.id.item_center_tv_date);
            TextView icon = itemView.findViewById(R.id.item_center_tv_con);
            TextView itemprangeTv = itemView.findViewById(R.id.item_center_tv_temp);
            ImageView iv = itemView.findViewById(R.id.item_center_iv);
//            获取对应天气情况
            WeatherBean.DataDTO.ForecastDTO dataBean = futureList.get(i);
            idateTv.setText(dataBean.getDate());
            icon.setText(dataBean.getType());
            itemprangeTv.setText(dataBean.getLow()+"~"+dataBean.getHigh());

        }
    }

    private  void initView(View view) {       //初始化键位视图
        trmpTv = view.findViewById(R.id.frag_tv_currenttemp);
        cityTv = view.findViewById(R.id.frag_tv_city);
        conditionTv = view.findViewById(R.id.frag_tv_condition);
        windTv = view.findViewById(R.id.frag_tv_wind);
        tempRangeTv = view.findViewById(R.id.frag_tv_temprange);
        dateTv = view.findViewById(R.id.frag_tv_date);
//        dayIv = view.findViewById(R.id.frag_iv_today);
        futureLayout = view.findViewById(R.id.frag_center_layout);
    }
}