#include "stdafx.h"

#include "../lwtask/main.hpp"

#include <boost/test/output_test_stream.hpp>
using boost::test_tools::output_test_stream;

using namespace::app;

namespace
{

void PaintNothing(shape_drawing_lib::CCanvasPainter& painter)
{
	using namespace shape_drawing_lib;

	CTriangle triangle({ 10, 15 }, { 100, 200 }, { 150, 250 });
	CRectangle rectangle({ 30, 40 }, 18, 24);
}

void PaintTriangle(shape_drawing_lib::CCanvasPainter& painter)
{
	using namespace shape_drawing_lib;

	CTriangle triangle({ 10, 15 }, { 100, 200 }, { 150, 250 });
	painter.Draw(triangle);
}

shape_drawing_lib::CCanvasPainter CreatePainter(output_test_stream & out)
{
	modern_graphics_lib::CModernGraphicsRenderer renderer(out);

	CModernGraphicsRendererAdapter adapter(renderer);
	return adapter;
}

}

struct StreamFixture
{
	output_test_stream output;
};

BOOST_FIXTURE_TEST_SUITE(CModernGraphicsRendererAdapter_, StreamFixture)

	BOOST_AUTO_TEST_CASE(bla)
	{
		auto painter = move(CreatePainter(output));
		PaintTriangle(painter);
	}

BOOST_AUTO_TEST_SUITE_END()
