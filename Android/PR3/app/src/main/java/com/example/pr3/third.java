package com.example.pr3;

import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link third#newInstance} factory method to
 * create an instance of this fragment.
 */
public class third extends Fragment {

    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    public third() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment Third.
     */
    // TODO: Rename and change types and number of parameters
    public static third newInstance(String param1, String param2) {
        third fragment = new third();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }
    TextView tv;
    View mView;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_third,container);
        mView = v;
        // Inflate the layout for this fragment
        return v;
    }
    public void setCourseText(String value)
    {
        tv=mView.findViewById(R.id.txtCourse);
        if (value.equals("B.Tech"))
        {
            tv.setText("You have Selected B.Tech Course");

        }
        else if (value.equals("M.Tech"))
        {
            tv.setText("You have Selected M.Tech Course");
        }
        else if (value.equals("BBA"))
        {
            tv.setText("You have Selected BBA Course");
        }
        else if (value.equals("B.Com"))
        {
            tv.setText("You have Selected B.Com Course");
        }
        else if (value.equals("B.Sc"))
        {
            tv.setText("You have Selected B.Sc Course");
        }
        else if (value.equals("M.Sc"))
        {
            tv.setText("You have Selected M.Sc Course");
        }
        else if (value.equals("B.PT"))
        {
            tv.setText("You have Selected B.PT Course");
        }
        else if (value.equals("B.Phrama"))
        {
            tv.setText("You have Selected B.Phrama Course");
        }
        else
        {
            tv.setText("None Selected");
        }

    }
}