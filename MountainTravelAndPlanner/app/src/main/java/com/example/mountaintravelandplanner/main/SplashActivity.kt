package com.example.mountaintravelandplanner.main

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import com.example.mountaintravelandplanner.R

class SplashActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        val timeOut = 4000
        val data = Intent(this@SplashActivity, MainActivity::class.java)
        Handler().postDelayed({
            startActivity(data)
            finish()
        }, timeOut.toLong())
    }
}