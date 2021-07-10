package com.example.weather3;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentStatePagerAdapter;

import java.util.List;

public class CityFragmentPagerAdapter extends FragmentStatePagerAdapter {
    List<Fragment> fragmentList;
    public CityFragmentPagerAdapter(FragmentManager fm,List<Fragment>fragmentList) {
        super(fm);
        this.fragmentList = fragmentList;
    }
    @Override
    public Fragment getItem(int position) {
        return fragmentList.get(position);
    }     //是第几个页面

    @Override
    public int getCount() {
        return fragmentList.size();
    }    //总页面数

    int childCount = 0;   //表示ViewPager包含的页数
    //    当ViewPager的页数发生改变时，必须要重写两个函数
    @Override
    public void notifyDataSetChanged() {       //提示更新
        this.childCount = getCount();
        super.notifyDataSetChanged();
    }

    @Override
    public int getItemPosition(@NonNull Object object) {
        if (childCount>0) {
            childCount--;
            return POSITION_NONE;
        }
        return super.getItemPosition(object);
    }
}
