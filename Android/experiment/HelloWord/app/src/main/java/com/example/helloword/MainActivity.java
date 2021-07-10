package com.example.helloword;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText phoneEdit, nameEdit;
    private Button register;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();

        register = (Button) findViewById(R.id.register);
        register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                register();
            }   //设置登录按钮
        });
    }
    private void init() {
        phoneEdit = (EditText) findViewById(R.id.phoneedit);    //初始化用户窗口
        nameEdit = (EditText) findViewById(R.id.nameedit);      //初始化密码窗口
    }
    public  void register() {      //用户名和密码不为空时，跳转到下一个页面
        //获取手机号码与昵称
        String phone = phoneEdit.getText().toString().trim();
        String name = nameEdit.getText().toString().trim();

        //手机号码和昵称均不可为空
        if (TextUtils.isEmpty(phone) || TextUtils.isEmpty(name)) {
            Toast.makeText(this, "选项不能为空", Toast.LENGTH_SHORT).show();
            return;
        }

        Intent intent =new Intent(this, MainActivity2.class);
        intent.putExtra("phone",phone);
        intent.putExtra("name",name);

        startActivity(intent);
    }
}