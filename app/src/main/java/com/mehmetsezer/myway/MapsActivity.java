package com.mehmetsezer.myway;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Switch;

public class MapsActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_attributes);
            }
    public void newPath(View view){
            Switch s1 = (Switch) findViewById(R.id.switch1);
            Switch s2 = (Switch) findViewById(R.id.switch1);
            Switch s3 = (Switch) findViewById(R.id.switch1);
            Intent intent=new Intent(getApplicationContext(),Attributes.class);
            intent.putExtra("switchsleepless",s1.isChecked());
            intent.putExtra("switchhungry",s2.isChecked());
            intent.putExtra("switchbreak",s3.isChecked());
            startActivity(intent);

            }
}
