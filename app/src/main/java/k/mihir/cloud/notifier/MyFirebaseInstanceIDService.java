package k.mihir.cloud.notifier;

import android.util.Log;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.FirebaseInstanceIdService;

public class MyFirebaseInstanceIDService extends FirebaseInstanceIdService {

    String token;
    private static final String TAG = "MyFirebaseInstanceIDSer";

    @Override
    public void onTokenRefresh() {
        super.onTokenRefresh();
        token= FirebaseInstanceId.getInstance().getToken();
        if(token!=null){
            Log.d(TAG,token);
        }
        else {
            Log.d(TAG," token not found.");
        }

    }

}
