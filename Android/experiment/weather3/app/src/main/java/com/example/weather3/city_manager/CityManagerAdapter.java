package com.example.weather3.city_manager;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.example.weather3.R;
import com.example.weather3.bean.WeatherBean;
import com.example.weather3.db.DatabaseBean;
import com.google.gson.Gson;

import java.util.List;

public class CityManagerAdapter extends BaseAdapter {
    Context context;
    List<DatabaseBean>mDatas;

    public CityManagerAdapter(Context context, List<DatabaseBean> mDatas) {  //从数据库里传入数据
        this.context = context;
        this.mDatas = mDatas;
    }
    @Override
    public Object getItem(int position) {
        return mDatas.get(position);
    }
    @Override
    public int getCount() {
        return mDatas.size();
//    return 1;
    }




    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {  //调用数据
        ViewHolder holder = null;
        if(convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.item_city_manager,null);
            holder = new ViewHolder(convertView);
            convertView.setTag(holder);
        }else {
            holder = (ViewHolder)convertView.getTag();
        }
        DatabaseBean bean = mDatas.get(position);
        holder.cityTv.setText(bean.getCity());


        WeatherBean weatherBean = new Gson().fromJson(bean.getContent(),WeatherBean.class);
//        获取今日天气情况
        WeatherBean.DataDTO.ForecastDTO dataBean = weatherBean.getData().getForecast().get(0);
//        weatherBean.getData().get 展示数据
        holder.conTv.setText("天气："+dataBean.getType());
        holder.currentTempTv.setText(weatherBean.getData().getWendu()+"℃");
        holder.windTv.setText(dataBean.getFengxiang());
        holder.tempRangeTv.setText(dataBean.getLow()+"~"+dataBean.getHigh());
        return convertView;
    }
    class ViewHolder {        //适配器个视图获取
        TextView cityTv,conTv,currentTempTv,windTv,tempRangeTv;
        public ViewHolder(View view) {
            cityTv = view.findViewById(R.id.item_city_tv_city);
            conTv = view.findViewById(R.id.item_city_tv_condition);
            currentTempTv = view.findViewById(R.id.item_city_tv_temp);
            windTv = view.findViewById(R.id.item_city_wind);
            tempRangeTv = view.findViewById(R.id.item_city_temprange);
        }
    }
}
