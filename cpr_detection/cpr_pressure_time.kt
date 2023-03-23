import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.mlkit.vision.common.InputImage
import com.google.mlkit.vision.pose.PoseDetection
import com.google.mlkit.vision.pose.PoseLandmark
import com.google.mlkit.vision.pose.Pose
import com.google.mlkit.vision.pose.defaults.PoseDetectorOptions
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    
    // Define initial state and count as list
    var temp = mutableListOf<String>("up")
    var count = mutableListOf<Int>(0)
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val options = PoseDetectorOptions.Builder()
                .setDetectorMode(PoseDetectorOptions.STREAM_MODE)
                .build()
        
        val poseDetector = PoseDetection.getClient(options)
        
        val image = InputImage.fromBitmap(bitmap, 0)
        
        poseDetector.process(image)
            .addOnSuccessListener { pose ->
                val poseLandmarks = pose.allPoseLandmarks
                
                // Get the coordinates of landmark 26, 15, and 25
                val landmarkLeftKnee = poseLandmarks[PoseLandmark.LEFT_KNEE]!!.position
                val landmarkLeftWrist = poseLandmarks[PoseLandmark.LEFT_WRIST]!!.position
                val landmarkRightKnee = poseLandmarks[PoseLandmark.RIGHT_KNEE]!!.position
                
                // Calculate the angle between landmark 26, 15, and 25
                val angle = calculateAngle(landmarkLeftKnee, landmarkLeftWrist, landmarkRightKnee)
                
                // Check if the angle is less than 90 degrees
                if (angle < 90) {
                    temp.add("up")
                }
                
                // Check if the angle is greater than 105 degrees
                else if (angle > 105) {
                    temp.add("down")
                    
                    // If the state of 'temp' changed from 'up' to 'down', increment 'count'
                    if (temp[temp.lastIndex - 1] == "up") {
                        count.add(count.last() + 1)
                    }
                }
                
                // If the angle is between 90 and 105 degrees
                else {
                    // Remove the 'Please pressure more' text if it is visible
                    if (temp.size > 1 && temp[temp.lastIndex - 1] == "down") {
                        // TODO: remove text from view
                    }
                    temp.add("up")
                }
                
                // Display the 'Please pressure more' text if the state of 'temp' is 'up'
                if (temp.last() == "up") {
                    // TODO: display text on view
                }
                
                // Display the count in the top left corner of the video
                countView.text = "Count: ${count.last()}"
            }
            .addOnFailureListener { e ->
                // TODO: handle failure
            }
        
    }
    
    // Define function to calculate angle between landmarks
    fun calculateAngle(a: PointF, b: PointF, c: PointF): Float {
        val radians = atan2(c.y - b.y, c.x - b.x) - atan2(a.y - b.y, a.x - b.x)
        var angle = abs(radians * 180.0 / PI.toFloat())
        if (angle > 180.0) {
            angle = 360 - angle
        }
        return angle
    }
}