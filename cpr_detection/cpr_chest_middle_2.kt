class PoseLandmarkView(context: Context, attrs: AttributeSet?) : View(context, attrs) {

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)

        //algorithms
				import android.graphics.Canvas
				import android.graphics.Color
				import android.graphics.Paint
				import com.google.mlkit.vision.pose.PoseLandmark
				
				// assuming you have already obtained a List<PoseLandmark> called "landmarks"
				
				// 1. Calculate the middle point between landmarks 11 and 12
				val landmarks = landmarks[PoseLandmark.LEFT_SHOULDER]
				val landmark12 = landmarks[PoseLandmark.RIGHT_SHOULDER]
				val midpoint1 = Pair((landmark11.position.x + landmark12.position.x) / 2f, (landmark11.position.y + landmark12.position.y) / 2f)
				
				// 2. Calculate the middle point between landmarks 23 and 24
				val landmark23 = landmarks[PoseLandmark.LEFT_HIP]
				val landmark24 = landmarks[PoseLandmark.RIGHT_HIP]
				val midpoint2 = Pair((landmark23.position.x + landmark24.position.x) / 2f, (landmark23.position.y + landmark24.position.y) / 2f)
				
				// 3. Calculate the 2/3 point coordinate between the two middle points which calculated process number 1 and 2
				val twoThirdsPoint = Pair((midpoint1.first * 2f / 3f + midpoint2.first * 1f / 3f), (midpoint1.second * 2f / 3f + midpoint2.second * 1f / 3f))
				
				// 4. Draw a green circle on the 2/3 point which calculated process number 3
				val paint = Paint().apply {
				    color = Color.GREEN
				    style = Paint.Style.FILL
				}
				val canvas: Canvas = your_canvas // replace with your own canvas
				canvas.drawCircle(twoThirdsPoint.first, twoThirdsPoint.second, 20f, paint) // replace 20f with your desired circle radius
    }
}