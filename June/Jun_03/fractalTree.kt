import javafx.application.Application
import javafx.scene.Group
import javafx.scene.Scene
import javafx.scene.canvas.Canvas
import javafx.scene.canvas.GraphicsContext
import javafx.scene.paint.Color
import javafx.stage.Stage
import kotlin.math.PI
import kotlin.math.cos
import kotlin.math.sin
import kotlin.random.Random

class FractalTree : Application() {
    override fun start(primaryStage: Stage) {
        primaryStage.title = "Fractal Tree"

        val root = Group()
        val canvas = Canvas(800.0, 600.0)
        val gc: GraphicsContext = canvas.graphicsContext2D

        drawFractalTree(gc, 400.0, 600.0, -PI / 2, 120.0, 10)

        root.children.add(canvas)
        primaryStage.scene = Scene(root)
        primaryStage.show()
    }

    private fun drawFractalTree(gc: GraphicsContext, x1: Double, y1: Double, angle: Double, length: Double, depth: Int) {
        if (depth == 0) return

        val x2 = x1 + length * cos(angle)
        val y2 = y1 + length * sin(angle)

        gc.stroke = Color.hsb(Random.nextDouble(360.0), 1.0, 1.0)
        gc.lineWidth = depth.toDouble()
        gc.strokeLine(x1, y1, x2, y2)

        drawFractalTree(gc, x2, y2, angle - Random.nextDouble(0.2, 0.5), length * Random.nextDouble(0.7, 0.9), depth - 1)
        drawFractalTree(gc, x2, y2, angle + Random.nextDouble(0.2, 0.5), length * Random.nextDouble(0.7, 0.9), depth - 1)
    }
}

fun main() {
    Application.launch(FractalTree::class.java)
}
