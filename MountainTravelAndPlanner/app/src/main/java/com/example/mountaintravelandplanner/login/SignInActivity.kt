package com.example.mountaintravelandplanner.login

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Patterns
import android.widget.Toast
import com.example.mountaintravelandplanner.databinding.ActivitySignInBinding
import com.example.mountaintravelandplanner.main.MainActivity
import com.google.firebase.auth.FirebaseAuth

class SignInActivity : AppCompatActivity() {

    lateinit var binding : ActivitySignInBinding
    lateinit var authentic : FirebaseAuth

    override fun onCreate(savedInstanceState: Bundle?) {
        binding = ActivitySignInBinding.inflate(layoutInflater)
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        authentic = FirebaseAuth.getInstance()

        binding.btnSignup.setOnClickListener {
            val intent = Intent(this, SignUpActivity::class.java)
            startActivity(intent)
        }
        binding.buttonSignin.setOnClickListener {
            val email = binding.editEmailSignin.text.toString()
            val password = binding.editPassSignin.text.toString()

            if(email.isEmpty()){
                binding.editEmailSignin.error = "email harus diisi"
                binding.editEmailSignin.requestFocus()
                return@setOnClickListener
            }
            if(!Patterns.EMAIL_ADDRESS.matcher(email).matches()){
                binding.editEmailSignin.error = "email tidak valid"
                binding.editEmailSignin.requestFocus()
                return@setOnClickListener
            }
            if(password.isEmpty()){
                binding.editPassSignin.error = "password harus diisi"
                binding.editPassSignin.requestFocus()
                return@setOnClickListener
            }

            signInFirebase(email,password)
        }
    }

    private fun signInFirebase(email: String, password: String) {
        authentic.signInWithEmailAndPassword(email,password)
            .addOnCompleteListener(this){
                if(it.isSuccessful){
                    Toast.makeText(this, "Selamat Datang $email", Toast.LENGTH_SHORT).show()
                    val intent = Intent(this, MainActivity::class.java)
                    startActivity(intent)
                }else{
                    Toast.makeText(this, "${it.exception?.message}", Toast.LENGTH_SHORT).show()
                }
            }
    }
}