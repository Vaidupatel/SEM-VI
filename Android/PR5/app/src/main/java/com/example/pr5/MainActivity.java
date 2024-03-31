package com.example.pr5;

import androidx.appcompat.app.AppCompatActivity;

import android.net.Uri;
import android.os.Bundle;
import android.widget.MediaController;
import android.widget.VideoView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        VideoView videoView = findViewById(R.id.videoView);

        String vPath = "android.resource://"+getPackageName()+"/raw/test_video";

        Uri videoUri = Uri.parse(vPath);

//        videoView.setVideoPath(vPath);
        videoView.setVideoURI(videoUri);
        videoView.start();

        MediaController mediaController = new MediaController(this);
        videoView.setMediaController(mediaController);
        mediaController.setAnchorView(videoView);


    }
}