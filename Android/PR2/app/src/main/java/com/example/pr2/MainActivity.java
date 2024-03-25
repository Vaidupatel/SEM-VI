package com.example.pr2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d("Activity Destroyed", "Activity Destroyed: ");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d("Activity Stopped", "Activity Stopped: ");

    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d("Activity Started", "Activity Started: ");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d("Activity Restarted", "Activity Restarted: ");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d("Activity Paused", "Activity Paused: ");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d("Activity Resumed", "Activity Resumed: ");
    }
}