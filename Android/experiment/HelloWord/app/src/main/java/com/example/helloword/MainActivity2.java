package com.example.helloword;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

public class MainActivity2 extends AppCompatActivity {

    private TextView phoneEdit, nameEdit;
    private Button nextPage;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        init();

        Intent intent = getIntent();
        String phone = intent.getStringExtra("phone");   //接收用户名输入内容
        String name = intent.getStringExtra("name");     //接收密码输入内容

        phoneEdit.setText(phone);       //显示用户名接收内容
        nameEdit.setText(name);         //显示密码接收内容

        nextPage.setOnClickListener(new View.OnClickListener() {   //跳转到下一个页面
            @Override
            public void onClick(View v) {
                Intent intent2 = new Intent(MainActivity2.this, MainActivity3.class);
                startActivity(intent2);
            }
        });
    }
    @SuppressLint("WrongViewCast")
    private void init() {        //初始化显示用户名，密码和前往下一页按钮
        phoneEdit = (TextView) findViewById(R.id.phoneedit2);
        nameEdit = (TextView) findViewById(R.id.nameedit2);
        nextPage = (Button) findViewById(R.id.NextPage);
    }

}