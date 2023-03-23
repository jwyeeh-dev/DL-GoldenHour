private var poseDetector: PoseDetector? = null

// Initialize the pose detector in onCreate or onCreateView
private fun initializePoseDetector() {
    val options = FirebaseVisionPoseDetectorOptions.Builder()
        .setDetectorMode(FirebaseVisionPoseDetectorOptions.STREAM_MODE)
        .build()

    poseDetector = FirebaseVision.getInstance().getPoseDetector(options)
}

// Call this function to process a new camera frame
private fun processCameraFrame(bitmap: Bitmap) {
    val image = FirebaseVisionImage.fromBitmap(bitmap)

    poseDetector?.detectInImage(image)
        ?.addOnSuccessListener { poses ->
            // Check if a pose was detected
            if (poses.isNotEmpty()) {
                val pose = poses[0]

                // Get the landmarks
                val landmarks = pose.allPoseLandmarks

                // Calculate the middle point between left shoulder and right shoulder
                val leftShoulder = landmarks[PoseLandmark.LEFT_SHOULDER]
                val rightShoulder = landmarks[PoseLandmark.RIGHT_SHOULDER]
                val shoulderMidpoint = PointF(
                    (leftShoulder.position.x + rightShoulder.position.x) / 2f,
                    (leftShoulder.position.y + rightShoulder.position.y) / 2f
                )

                // Calculate the middle point between left hip and right hip
                val leftHip = landmarks[PoseLandmark.LEFT_HIP]
                val rightHip = landmarks[PoseLandmark.RIGHT_HIP]
                val hipMidpoint = PointF(
                    (leftHip.position.x + rightHip.position.x) / 2f,
                    (leftHip.position.y + rightHip.position.y) / 2f
                )

                // Calculate the 2/3 point between the shoulder and hip midpoints
                val x = (2 * shoulderMidpoint.x + hipMidpoint.x) / 3f
                val y = (2 * shoulderMidpoint.y + hipMidpoint.y) / 3f

                // Draw a green circle on the 2/3 point
                val canvas = SurfaceHolder.lockCanvas()
                val paint = Paint()
                paint.color = Color.GREEN
                canvas.drawCircle(x, y, 10f, paint)
                SurfaceHolder.unlockCanvasAndPost(canvas)
            }
        }
        ?.addOnFailureListener { e ->
            // Handle the failure
        }
}