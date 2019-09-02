#pragma once

#include <array>
#include <boost/format.hpp>
#include <boost/optional.hpp>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

// ������������ ���� ����������� ���������� (���������� ��� ���������)
namespace graphics_lib
{
// ����� ��� ���������
class ICanvas
{
public:
	// ������ "����" � ����� x, y
	virtual void MoveTo(int x, int y) = 0;
	// ������ ����� � ������� �������, ���������� ���� � ����� x,y
	virtual void LineTo(int x, int y) = 0;
	virtual ~ICanvas() = default;
};

// ���������� ������ ��� ���������
class CCanvas : public ICanvas
{
public:
	void MoveTo(int x, int y) override
	{
		cout << "MoveTo (" << x << ", " << y << ")" << endl;
	}
	void LineTo(int x, int y) override
	{
		cout << "LineTo (" << x << ", " << y << ")" << endl;
	}
};
} // namespace graphics_lib

// ������������ ���� ���������� ��� ��������� ����� (���������� graphics_lib)
// ��� ���������� ���������� ��� ���������
namespace shape_drawing_lib
{
struct Point
{
	int x;
	int y;
};

// ��������� ��������, ������� ����� ���� ���������� �� ������ �� graphics_lib
class ICanvasDrawable
{
public:
	virtual void Draw(graphics_lib::ICanvas& canvas) const = 0;
	virtual ~ICanvasDrawable() = default;
};

class CTriangle : public ICanvasDrawable
{
public:
	CTriangle(const Point& p1, const Point& p2, const Point& p3)
		: m_points({ p1, p2, p3 })
	{
	}

	void Draw(graphics_lib::ICanvas& canvas) const override
	{
		canvas.MoveTo(m_points[2].x, m_points[2].y);
		for (const auto& point : m_points)
		{
			canvas.LineTo(point.x, point.y);
		}
	}

private:
	array<Point, 3> m_points;
};

class CRectangle : public ICanvasDrawable
{
public:
	CRectangle(const Point& leftTop, int width, int height)
		: m_leftTop(leftTop)
		, m_width(width)
		, m_height(height)
	{
	}

	void Draw(graphics_lib::ICanvas& canvas) const override
	{
		canvas.MoveTo(m_leftTop.x, m_leftTop.y);
		canvas.LineTo(m_leftTop.x + m_width, m_leftTop.y);
		canvas.LineTo(m_leftTop.x + m_width, m_leftTop.y - m_height);
		canvas.LineTo(m_leftTop.x, m_leftTop.y - m_height);
		canvas.LineTo(m_leftTop.x, m_leftTop.y);
	}

private:
	Point m_leftTop;
	int m_width;
	int m_height;
};

class CCanvasPainter
{
public:
	CCanvasPainter(graphics_lib::ICanvas& canvas)
		: m_canvas(canvas)
	{
	}

	void Draw(const ICanvasDrawable& drawable)
	{
		drawable.Draw(m_canvas);
	}

private:
	graphics_lib::ICanvas& m_canvas;
};
} // namespace shape_drawing_lib

// ������������ ���� ����������� ����������� ���������� (���������� ��� ���������)
namespace modern_graphics_lib
{
class CPoint
{
public:
	CPoint(int x, int y)
		: x(x)
		, y(y)
	{
	}

	int x;
	int y;
};

// ����� ��� ������������ ��������� �������
class CModernGraphicsRenderer
{
public:
	CModernGraphicsRenderer(ostream& strm)
		: m_out(strm)
	{
	}

	~CModernGraphicsRenderer()
	{
		if (m_drawing) // ��������� ���������, ���� ��� ���� ������
		{
			EndDraw();
		}
	}

	// ���� ����� ������ ���� ������ � ������ ���������
	void BeginDraw()
	{
		if (m_drawing)
		{
			throw logic_error("Drawing has already begun");
		}
		m_out << "<draw>" << endl;
		m_drawing = true;
	}

	// ��������� ��������� �����
	void DrawLine(const CPoint& start, const CPoint& end)
	{
		if (!m_drawing)
		{
			throw logic_error("DrawLine is allowed between BeginDraw()/EndDraw() only");
		}
		m_out << boost::format(R"(<line fromX="%1%" fromY="%2%" toX="%3%" toY="%4%"/>)") % start.x % start.y % end.x % end.y << endl;
		// NOTE: ������� ����� 2
	}

	// ���� ����� ������ ���� ������ � ����� ���������
	void EndDraw()
	{
		if (!m_drawing)
		{
			throw logic_error("Drawing has not been started");
		}
		m_out << "</draw>" << endl;
		m_drawing = false;
	}

private:
	ostream& m_out;
	bool m_drawing = false;
};
} // namespace modern_graphics_lib

namespace graphics_lib_pro
{
// ����� ��� ���������
class ICanvas
{
public:
	// ��������� ����� � ������� 0xRRGGBB
	virtual void SetColor(uint32_t rgbColor) = 0;
	virtual void MoveTo(int x, int y) = 0;
	virtual void LineTo(int x, int y) = 0;
	virtual ~ICanvas() = default;
};

// ���������� ������ ��� ���������
class CCanvas : public ICanvas
{
public:
	void SetColor(uint32_t rgbColor) override
	{
		if (rgbColor > 16777215)
		{
			throw out_of_range("Color chould be in range [0, 2**24 - 1]");
		}
		cout << hex << '#' << rgbColor << endl;
	}
	void MoveTo(int x, int y) override
	{
		cout << "MoveTo (" << x << ", " << y << ")" << endl;
	}
	void LineTo(int x, int y) override
	{
		cout << "LineTo (" << x << ", " << y << ")" << endl;
	}
};
} // namespace graphics_lib_pro

// ������������ ���� ����������� ����������� ����������� ���������� (���������� ��� ���������)
namespace modern_graphics_lib_pro
{
class CPoint
{
public:
	CPoint(int x, int y)
		: x(x)
		, y(y)
	{
	}

	int x;
	int y;
};

// ���� � ������� RGBA, ������ ��������� ��������� �������� �� 0.0f �� 1.0f
class CRGBAColor
{
public:
	CRGBAColor(float r, float g, float b, float a)
		: r(r)
		, g(g)
		, b(b)
		, a(a)
	{
	}
	float r, g, b, a;
};

// ����� ��� ������������ ��������� �������
class CModernGraphicsRenderer
{
public:
	CModernGraphicsRenderer(ostream& strm)
		: m_out(strm)
	{
	}

	~CModernGraphicsRenderer()
	{
		if (m_drawing)
		{
			EndDraw();
		}
	}

	// ���� ����� ������ ���� ������ � ������ ���������
	void BeginDraw()
	{
		if (m_drawing)
		{
			throw logic_error("Drawing has already begun");
		}
		m_out << "<draw>" << endl;
		m_drawing = true;
	}

	// ��������� ��������� �����
	void DrawLine(const CPoint& start, const CPoint& end, const CRGBAColor& color)
	{
		if (!m_drawing)
		{
			throw logic_error("DrawLine is allowed between BeginDraw()/EndDraw() only");
		}
		m_out << boost::format(R"(<line fromX="%1%" fromY="%2" toX="%3%" toY="%4%"/>)") % start.x % start.y % end.x % end.y << endl;
		m_out << boost::format(R"(  <color r="%1" g="%2" b="%3" a="%4" />)") % color.r % color.g % color.b % color.a << endl;
		m_out << "</line>" << endl;
	}

	// ���� ����� ������ ���� ������ � ����� ���������
	void EndDraw()
	{
		if (!m_drawing)
		{
			throw logic_error("Drawing has not been started");
		}
		m_out << "</draw>" << endl;
		m_drawing = false;
	}

private:
	ostream& m_out;
	bool m_drawing = false;
};
} // namespace modern_graphics_lib_pro

// ������������ ���� ���������� (�������� ��� �����������)
namespace app
{
class CModernGraphicsRendererAdapter
	: public graphics_lib::ICanvas
{
public:
	CModernGraphicsRendererAdapter(modern_graphics_lib::CModernGraphicsRenderer& renderer)
		: m_renderer(renderer)
		, m_point(boost::none)
	{
		m_renderer.BeginDraw();
	}

	void MoveTo(int x, int y) override
	{
		m_point = modern_graphics_lib::CPoint(x, y);
	}

	void LineTo(int x, int y) override
	{
		m_renderer.DrawLine(m_point.get(), { x, y });
		MoveTo(x, y);
	}

private:
	modern_graphics_lib::CModernGraphicsRenderer& m_renderer;
	boost::optional<modern_graphics_lib::CPoint> m_point;
};

void PaintPicture(shape_drawing_lib::CCanvasPainter& painter)
{
	using namespace shape_drawing_lib;

	// NOTE: ��� ������ ��������� �����? ��� ��� ���, ��� � ��� �������� �������? �� ������ ������ - �����.
	CTriangle triangle({ 10, 15 }, { 100, 200 }, { 150, 250 });
	CRectangle rectangle({ 30, 40 }, 18, 24);

	painter.Draw(triangle);
	painter.Draw(rectangle);
}

void PaintPictureOnCanvas()
{
	graphics_lib::CCanvas simpleCanvas;
	shape_drawing_lib::CCanvasPainter painter(simpleCanvas);
	PaintPicture(painter);
}

void PaintPictureOnModernGraphicsRenderer()
{
	modern_graphics_lib::CModernGraphicsRenderer renderer(cout);

	CModernGraphicsRendererAdapter adapter(renderer);
	shape_drawing_lib::CCanvasPainter painter(adapter);
	PaintPicture(painter);
}
} // namespace app
