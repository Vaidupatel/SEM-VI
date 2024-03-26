package com.example.pr4;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    EditText userName,email,dob,phone,address,password;
    Button signup,Delete;
    DBHelper DB;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        userName = findViewById(R.id.userName);
        password = findViewById(R.id.password);

        Delete = findViewById(R.id.delete);
        signup = findViewById(R.id.signup);

        DB = new DBHelper(this);

        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String Username = userName.getText().toString();
                String Password = password.getText().toString();

                if(Username.equals("")||Password.equals(""))
                    Toast.makeText(MainActivity.this,"Please Enter all the fields",Toast.LENGTH_LONG).show();
                else{
                    Boolean checkuser = DB.checkusername(Username);
                    if(checkuser == false){
                        Boolean insert = DB.insertData(Username,Password);
                        if(insert == true){
                            Toast.makeText(MainActivity.this,"Registered Successfully",Toast.LENGTH_LONG).show();
                            Intent intent = new Intent(getApplicationContext(),HomeActivity.class);
                            intent.putExtra("USERNAME_EXTRA", Username);
                            startActivity(intent);
                        }else{
                            Toast.makeText(MainActivity.this,"Registered Failed",Toast.LENGTH_LONG).show();
                        }
                    }else{
                            Toast.makeText(MainActivity.this,"User already exist! Please Sign in",Toast.LENGTH_LONG).show();
                    }
                }

            }
        });

        Delete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                Intent intent = new Intent(getApplicationContext(),LoginActivity.class);
//                startActivity(intent);
                String Username = userName.getText().toString();
                String Password = password.getText().toString();
                if(Username.equals("")||Password.equals(""))
                    Toast.makeText(MainActivity.this,"Please Enter all the fields",Toast.LENGTH_LONG).show();
                else{
                    Boolean checkuser = DB.checkusername(Username);
                    if(checkuser == true){
                        Boolean delete = DB.deleteData(Username);
                        if(delete == true){
                            Toast.makeText(MainActivity.this,"Deleted Successfully",Toast.LENGTH_LONG).show();
                            Intent intent = new Intent(getApplicationContext(),HomeActivity.class);
                            startActivity(intent);
                        }else{
                            Toast.makeText(MainActivity.this,"Deletion Failed",Toast.LENGTH_LONG).show();
                        }
                    }else{
                        Toast.makeText(MainActivity.this,"User not exist! Please Sign up first",Toast.LENGTH_LONG).show();
                    }
                }
            }
        });

    }
}